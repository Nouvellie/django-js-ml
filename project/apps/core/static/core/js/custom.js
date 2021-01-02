var app = angular.module("coreAng", []);
app.config(function ($interpolateProvider) {
    'use strict';
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller("coreController", function ($http, $scope) {
    'use strict';
    console.log('custom js');
});