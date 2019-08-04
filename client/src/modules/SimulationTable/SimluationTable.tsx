import React, { useEffect, useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { Table } from 'semantic-ui-react'
import _ from 'lodash';
import { BASE_API_URL } from '../../constants/constants';

const ZERO_TO_TWELVE = _.range(0,13);
const NUM_OF_SIMS = 4000 // MUST MATCH BACKEND OR BE PASSED TO BACKEND

const getColor = (value: number) => {
  var hue=(value*120).toString(10);
  return ["hsl(",hue,",80%,60%)"].join("");
}

const sortTableByX = (x: number, tableData: TableData, updateTable: (state: State) => void) => {
  const tableDataSortedByX = _.sortBy(tableData, ({ cumulativePercentages }) => cumulativePercentages[x]).reverse();
  updateTable({ pageStatus: 'hasData', tableData: tableDataSortedByX });
};

type TableData = Array<{ team: string, cumulativePercentages: Array<number>}>;
type SeasonSimulation = { [key: string]: number };
type TeamSimulationObj = { 'conference_results': SeasonSimulation, 'non_conference_results': SeasonSimulation, 'total_wins': SeasonSimulation };
type SimulateResponse = { [key: string]: TeamSimulationObj };

// {_.map(tableData, ({ team, ...rest }) => {
//   const likelihoodOfExactlyXWins = _.map(ONE_TO_TWELVE, x => Number(rest[x]) / NUM_OF_SIMS);
//   // @ts-ignore
//   const cumulativePercentages = likelihoodOfExactlyXWins.reduce((acc, cv, idx) => [...acc, cv + (acc[idx - 1] || 0)], []).map(x => 1 - x)
//   return (
//     <Table.Row>
//       <Table.Cell>{team}</Table.Cell>
//       {_.map(cumulativePercentages, x => <Table.Cell style={{ backgroundColor: getColor(x) }}>{`${(x * 100).toFixed(1)}%`}</Table.Cell>)}
//     </Table.Row>
//   );
// })}

const transformSimulateResponse = (data: SimulateResponse): TableData  => _.map(data, (v, k) => {
  const simulationResults = { ...v.total_wins };
  const likelihoodOfExactlyXWins = _.map(ZERO_TO_TWELVE, x => Math.round((Number(simulationResults[x]) / NUM_OF_SIMS) * 1000) / 1000);
  
  const cumulativePercentages = likelihoodOfExactlyXWins.reduce(
    // @ts-ignore
    (acc, cv, idx) => [...acc, cv + (acc[idx - 1] || 0)], [],
  ).map((x: number) => Math.round((1 - x) * 100) / 100);

  // let runningSum = 0;
  // const cumulativePercentages = _.map(likelihoodOfExactlyXWins, (val) => {
  //   runningSum += val
  //   return runningSum
  // })

  console.log({ k, likelihoodOfExactlyXWins, cumulativePercentages  });
  return { team: k, cumulativePercentages };
});

type State = { pageStatus: string, tableData: TableData };
const SimulationTable: React.FC = () => {
  const [{ pageStatus, tableData }, updateTable] = useState<State>({ pageStatus: "Loading...", tableData: [] });

  useEffect(() => {
    axios
      // TODO move all API logic to an \`api` file
      .get(`${BASE_API_URL}/simulate`, { 'params': { 'year': 2019 }})
      .then((data: AxiosResponse) => {
        const tableData = transformSimulateResponse(data.data)
        updateTable({ pageStatus: 'hasData', tableData })
      })
      .catch(() => updateTable({ pageStatus: 'error', tableData: [] }))
  }, [])

  if (pageStatus === "Loading...") {
    return <p>Loading...</p>
  }

  if (pageStatus === "error") {
    return <p>Error!!</p>
  }

  if (pageStatus === "hasData") {
    return (
      <Table sortable celled fixed>
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell width={3}>Team Name</Table.HeaderCell>
              {_.map(ZERO_TO_TWELVE, x => <Table.HeaderCell key={x} onClick={() => sortTableByX(x, tableData, updateTable)}>{x}</Table.HeaderCell>)}
            </Table.Row>
          </Table.Header>
          <Table.Body>
            {_.map(tableData, ({ team, cumulativePercentages }) => {
              return (
                <Table.Row>
                  <Table.Cell>{team}</Table.Cell>
                  {_.map(cumulativePercentages, x => <Table.Cell style={{ backgroundColor: getColor(x) }}>{`${(x * 100).toFixed(1)}%`}</Table.Cell>)}
                </Table.Row>
              );
            })}
          </Table.Body>
        </Table>
    );
  }
  return null;
}

export default SimulationTable;
