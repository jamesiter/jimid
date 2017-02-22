var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ViewEncapsulation } from '@angular/core';
import { AuthService } from "../core/auth.service";
import { Router } from "@angular/router";
import { LoginUser } from "./login-user";
import { Observable } from "rxjs";
import { Http } from "@angular/http";
import { GlobalService } from "../core/global.service";
export var LoginComponent = (function () {
    function LoginComponent(http, gs, router, authService) {
        this.http = http;
        this.gs = gs;
        this.router = router;
        this.authService = authService;
        this.loginUser = new LoginUser();
    }
    LoginComponent.prototype.ngOnInit = function () {
    };
    LoginComponent.prototype.ngAfterViewInit = function () {
        this.auth();
    };
    LoginComponent.prototype.auth = function () {
        var _this = this;
        var sc = this.authService.auth().subscribe(function (req) {
            if (req.status == 200) {
                _this.authService.isLoggedIn = true;
                console.log('Auth succeed!');
                _this.router.navigate([_this.authService.redirectUrl], { queryParams: _this.authService.redirectQueryParams });
            }
            else if (req.status == 278) {
                var body = req.json();
                // window.location.href = body['redirect']['location'];
                _this.router.navigate(['/login']);
            }
            sc.unsubscribe();
        }, function (err) {
            console.log('Auth failed!');
            console.log(err);
        }, function () {
            console.log('Auth complete!');
            console.log(_this.authService.isLoggedIn);
        });
    };
    LoginComponent.prototype.login = function () {
        var _this = this;
        var sc = this.authService.login('login_name', this.loginUser.password, this.loginUser.login_name, this.loginUser.mobile_phone, this.loginUser.email).subscribe(function (req) {
            if (req.status == 200) {
                _this.authService.isLoggedIn = true;
                _this.router.navigate(['/']);
                console.log('Login succeed!');
            }
            else {
                _this.authService.isLoggedIn = false;
                _this.router.navigate(['/login']);
            }
            sc.unsubscribe();
        }, function (err) {
            _this.authService.isLoggedIn = false;
            _this.router.navigate(['/login']);
            console.log('Login failed!');
            console.log(err);
            return Observable.throw(err);
        }, function () {
            console.log('Login complete!');
        });
    };
    LoginComponent = __decorate([
        Component({
            selector: 'app-login',
            templateUrl: './login.component.html',
            styleUrls: [
                '../../vendors/bootstrap/dist/css/bootstrap.min.css',
                '../../vendors/font-awesome/css/font-awesome.min.css',
                '../../vendors/nprogress/nprogress.css',
                '../../vendors/animate.css/animate.min.css',
                '../../assets/src/scss/custom.css',
                './login.component.css',
            ],
            encapsulation: ViewEncapsulation.Native
        }), 
        __metadata('design:paramtypes', [Http, GlobalService, Router, AuthService])
    ], LoginComponent);
    return LoginComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/login/login.component.js.map