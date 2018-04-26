login.controller("Registration1Controller", function($scope, $state, $commonFactories, $rootScope) {
    console.log("In-Registration1  controller");


    $scope.NextButtonAction = function() {
        // console.log("first name value:", $scope.firstName);
        $state.go("Registration_2");
    }



    $rootScope.Registration = function() {
        try {
            var payload = {
                "First_name": $scope.firstName,
                "Last_name": $scope.LastName,
                "date_of_birth": $scope.bday,
                "email_id": $scope.emailId,
                "employee_id": $scope.employeeId,
                "Password": $scope.Password,
                "mobile_number": $scope.mobileno,
                "Gender": $scope.male || $scope.female,
                "City": $scope.cityname,
                "State": $scope.stateName,
                "Country": $scope.countryName
            }
            console.log(payload);
            $commonFactories.Registration(payload)
                .then(function successCallback(response) {
                    console.log(response.data.status);
                    if (response.data) {
                        $scope.loginResponceData = response.data;

                        console.log("Responce for login in (loginUserAuthentication):", $scope.loginResponceData);

                        // $state.go("Registration_2");

                    } else {
                        console.log("Responce for login in:", $scope.loginResponceData);
                        $rootScope.isUserLoggedIn = true;
                    }
                });
        } catch (err) {
            console.log(err);
        }
    }







});