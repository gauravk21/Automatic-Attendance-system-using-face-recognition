login.factory('$commonFactories', function($http) {

    var factory = {};

    factory.Registration = function(payload) {
        return $http({
            method: 'POST',
            url: "http://localhost:3000/Registration",
            data: payload
        });
    };

    return factory;

})