var ruckusTool	 = angular.module('workTojob', []);


ruckusTool.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});



ruckusTool.controller("JobDetailPage", function($scope, $http) {

  $scope.close_job_position_popup = function() {
    $('#myModal').modal('show');
  }







})





