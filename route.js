angular.module("App").config(function($routeProvider){
	$routeProvider.when("/", {
			template: "<h1 align='center'>Hello friend!</h1>"
		});
	$routeProvider.when("/cadastro", {
			templateUrl: "cadastro.html",
			controllerUrl: "cadastroCtrl"
		});
	$routeProvider.when("/login",{
			templateUrl: "login.html",
			controllerUrl: "loginCtrl.js"
		});
	$routeProvider.when("/perfil",{
			templateUrl: "perfil.html",
			controllerUrl: "perfilCtrl.js"
		});
});