login.controller("Registration2Controller", function($scope, $state, $commonFactories, $rootScope) {
    console.log("In-Registration2  controller");


    $scope.tempcall = function() {
        $rootScope.Registration();

    }


    $scope.gotoHome = function() {
        $state.go("Home");
    }

});