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

/***/ "./src/update_token.js":
/*!*****************************!*\
  !*** ./src/update_token.js ***!
  \*****************************/
/***/ (() => {

eval("console.log('update_token.js is loaded!');\nwindow.updateToken = function () {\n  // console.log('Old Token: ', authToken);\n  var oldAuthToken = localStorage.getItem('authToken');\n  fetch('http://127.0.0.1:8000/api/update_token/', {\n    method: 'POST',\n    headers: {\n      'Authorization': 'Token ' + oldAuthToken,\n      'Content-Type': 'application/json'\n    }\n  }).then(function (response) {\n    return response.json();\n  }).then(function (data) {\n    console.log('New Token:', data.new_token);\n    // Обновляем токен на странице\n    document.getElementById('authToken').innerText = data.new_token;\n    // Обновляем токен на клиенте, сохраняем новый токен в localStorage\n    localStorage.setItem('authToken', data.new_token);\n  })[\"catch\"](function (error) {\n    return console.error('Error:', error);\n  });\n};\nfunction aaa() {\n  console.log('aaa called');\n}\n\n//# sourceURL=webpack://frontend/./src/update_token.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/update_token.js"]();
/******/ 	
/******/ })()
;