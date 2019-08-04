import React, { useEffect, useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { Table } from 'semantic-ui-react'
import _ from 'lodash';
import { BASE_API_URL } from '../../constants/constants';
// TODO: Figure out how to use path properly
// import path from 'path';

const [ENTROPY, FPI, MASSEY, SP_PLUS, AVERAGE] = ['ENTROPY', 'FPI', 'MASSEY', 'SP_PLUS', 'AVERAGE'];

type State = { pageStatus: string, teamRatings: {} | null }
type TableState = { column: string | null , data: [], direction: string | null };
const SimulationTable: React.FC = () => {
  const [{ pageStatus, teamRatings }, setApiStatus] = useState<State>({ pageStatus: "Loading...", teamRatings: null });

  useEffect(() => {
    axios
      // TODO move all API logic to an \`api` file
      .get(`${BASE_API_URL}/simulate`, { 'params': { 'year': 2019 }})
      .then((data: AxiosResponse) => {
        console.log(data);
        setApiStatus({ pageStatus: 'hasData', teamRatings: data.data })
      })
      .catch(() => setApiStatus({ pageStatus: 'error', teamRatings: null }))
  }, [])

  let pageContent;

  if (pageStatus === "Loading...") {
    return <p>Loading...</p>
  }

  if (pageStatus === "error") {
    return <p>Error!!</p>
  }

  if (pageStatus === "hasData") {
    const teamArr = _.map(
      teamRatings,
      (ratings: {}, team) => ({ 'team': team, [AVERAGE]: _.round(_.sum(_.map(ratings, r => r)) / 4, 2), ...ratings }),
    );

    pageContent = (
      <Table sortable celled fixed>
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell
                // sorted={column === 'TeamName' ? direction : null}
                // onClick={this.handleSort('name')}
              >
                Team Name
              </Table.HeaderCell>
              <Table.HeaderCell
                // sorted={column === ENTROPY ? direction : null}
                // onClick={this.handleSort('age')}
              >
                Entropy
              </Table.HeaderCell>
              <Table.HeaderCell
                // sorted={column === FPI ? direction : null}
                // onClick={this.handleSort('gender')}
              >
                FPI
              </Table.HeaderCell>
              <Table.HeaderCell
                // sorted={column === MASSEY ? direction : null}
                // onClick={this.handleSort('gender')}
              >
                MASSEY
              </Table.HeaderCell>
              <Table.HeaderCell
                // sorted={column === SP_PLUS ? direction : null}
                // onClick={this.handleSort('gender')}
              >
                SP+
              </Table.HeaderCell>
              <Table.HeaderCell
                // sorted={column === AVERAGE ? direction : null}
                // onClick={this.handleSort('gender')}
              >
                Average Rating
              </Table.HeaderCell>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            {_.map(teamArr, (obj) => (
              <Table.Row key={obj.team}>
                <Table.Cell>{obj.team}</Table.Cell>
                <Table.Cell>{_.get(obj, ENTROPY)}</Table.Cell>
                <Table.Cell>{_.get(obj, FPI)}</Table.Cell>
                <Table.Cell>{_.get(obj, SP_PLUS)}</Table.Cell>
                <Table.Cell>{_.get(obj, MASSEY)}</Table.Cell>
                <Table.Cell>{_.get(obj, AVERAGE)}</Table.Cell>
              </Table.Row>
            ))}
          </Table.Body>
        </Table>
    );
  }

  return (
    <div>
      <header>
        {pageContent}
      </header>
    </div>
  );
}

export default SimulationTable;
