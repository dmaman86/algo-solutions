module.exports = {
  transform: {
    "^.+\\.js$": "babel-jest", // Usa Babel para transformar archivos JS
  },
  testMatch: [
    "**/tests/__tests__/**/*.test.js", // Busca archivos de prueba en __tests__
  ],
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/problems/$1", // Alias '@' apunta a la carpeta 'problems'
  },
  moduleDirectories: ["node_modules", "<rootDir>"], // Busca módulos en node_modules y en la raíz del proyecto
  collectCoverageFrom: [
    "problems/**/*.js", // Incluye archivos JS de 'problems' para cobertura
    "!**/node_modules/**", // Excluye node_modules
    "!**/tests/**", // Excluye carpetas de pruebas
  ],
  coverageDirectory: "<rootDir>/coverage", // Directorio de informes de cobertura
};
