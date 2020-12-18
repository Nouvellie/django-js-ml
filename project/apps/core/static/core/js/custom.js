var app = angular.module("leagueStats", []);
app.config(function ($interpolateProvider) {
    'use strict';
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller("leagueStatsController", function ($http, $scope) {
    'use strict';
    $scope.warning = false;
    $scope.danger = false;
    $scope.notregistered = false;
    $scope.api_error = false;
    $scope.template = false;
    $scope.loading = false;
    $scope.solo_q_bool = false;
    $scope.solo_q_bool = false;
    $scope.searchSummoner = function () {
        $scope.danger = false;
        $scope.notregistered = false;
        $scope.api_error = false;
        $scope.template = false;
        $scope.loading = true;
        if (!$scope.summonerName || !$scope.summonerRegion) {
            $scope.loading = false;
            $scope.warning = true;
        } else {
            $scope.warning = false;
            $scope.template = false;
            var data = {
                nick: $scope.summonerName,
                region: $scope.summonerRegion
            };
            $http.post('/profile-api/', data).then(function successCallback(response) {
                $scope.loading = false;
                $scope.template = true;
                $scope.summoner = response.data.summoner;
                $scope.flex_bool = response.data.flex_bool;
                if ($scope.flex_bool) {
                    $scope.flex = response.data.flex;
                }
                $scope.solo_q_bool = response.data.solo_q_bool;
                if ($scope.solo_q_bool) {
                    $scope.solo_q = response.data.solo_q;
                }
                $scope.extra = response.data.extra;
            }, function errorCallback(response) {
                $scope.loading = false;
                if (response.status === 404) {
                    $scope.danger = true;
                } else if (response.status === 400) {
                    $scope.notregistered = true;
                } else if (response.status === 403) {
                    $scope.api_error = true;
                } else {
                    console.log("Error.");
                }

            });
        }
    };
});