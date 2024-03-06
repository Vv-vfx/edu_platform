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

/***/ "./src/requests_by_token.js":
/*!**********************************!*\
  !*** ./src/requests_by_token.js ***!
  \**********************************/
/***/ (() => {

eval("// Использование токена для запросов к API\nfunction fetchDataWithToken(token) {\n  return fetch('http://localhost:8000/api/course/', {\n    method: 'GET',\n    headers: {\n      'Authorization': 'Token ' + token,\n      'Content-Type': 'application/json'\n    }\n  }).then(function (response) {\n    return response.json();\n  }).then(function (data) {\n    return console.log(data);\n  })[\"catch\"](function (error) {\n    return console.error('Error:', error);\n  });\n}\nwindow.fetchResponce = function (authToken) {\n  if (authToken) {\n    fetchDataWithToken(authToken);\n  } else {\n    console.error('No token received');\n  }\n};\n\n//# sourceURL=webpack://frontend/./src/requests_by_token.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/requests_by_token.js"]();
/******/ 	
/******/ })()
;