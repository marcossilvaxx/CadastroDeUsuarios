angular.module("App", ["ngRoute"]);
angular.module("App").controller("cadastroCtrl", function($scope, $http){

	$scope.cadastro = function(usuario){
		$http.post("http://127.0.0.1:5000/user", usuario).then(function(success){
			$scope.req = "deu certo";
		}, function(error){
			$scope.req = "deu errado";
		});
	};
});