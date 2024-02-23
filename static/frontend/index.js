/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/index.js":
/*!**********************!*\
  !*** ./src/index.js ***!
  \**********************/
/***/ (() => {

eval("alert(\"Скрипт запустился\");\nvar url = 'http://localhost:8000/api/course/';\n// const accessToken = 'your_access_token';\n\nfetch(url, {\n  method: 'GET',\n  // Метод HTTP запроса\n  headers: {\n    'Authorization': \"Bearer \".concat(accessToken),\n    // Включение токена доступа в заголовки\n    'Content-Type': 'application/json'\n  }\n}).then(function (response) {\n  if (!response.ok) {\n    throw new Error(\"HTTP error! status: \".concat(response.status));\n  }\n  return response.json(); // Преобразование ответа в JSON\n}).then(function (data) {\n  console.log(data); // Вывод полученных данных в консоль\n})[\"catch\"](function (error) {\n  console.error('There was an error fetching the courses:', error);\n});\n\n//# sourceURL=webpack://frontend/./src/index.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/index.js"]();
/******/ 	
/******/ })()
;