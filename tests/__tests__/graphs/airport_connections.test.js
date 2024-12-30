import { airportConnections } from "@/graphs/airport_connections/js/airport_connections";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/graphs/airports_connections.json";

describe("Airport Connections", () => {
  testCases.forEach(({ airports, routes, startingAirport, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = airportConnections(airports, routes, startingAirport);
      expect(result).toEqual(expected);
    });
  });
});
