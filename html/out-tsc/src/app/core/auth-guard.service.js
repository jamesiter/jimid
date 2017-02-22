/**
 * Created by James on 2016/12/16.
 */
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';
export var AuthGuard = (function () {
    function AuthGuard(router, authService) {
        this.router = router;
        this.authService = authService;
    }
    AuthGuard.prototype.ngOnDestroy = function () {
    };
    AuthGuard.prototype.canActivate = function (activatedRouteSnapshot, state) {
        var url = state.url;
        var queryParams = {};
        for (var key in activatedRouteSnapshot.queryParams) {
            queryParams[key] = activatedRouteSnapshot.queryParams[key];
        }
        return this.checkLogin(url, queryParams);
    };
    AuthGuard.prototype.checkLogin = function (url, queryParams) {
        if (this.authService.isLoggedIn) {
            return true;
        }
        // Store the attempted URL for redirecting
        this.authService.redirectUrl = url.split('?')[0];
        this.authService.redirectQueryParams = queryParams;
        // Navigate to the login page with extras
        // this.router.navigate(['/', {outlets: {'all-page': ['login']}}]);
        this.router.navigate(['/login']);
        return false;
    };
    AuthGuard.prototype.canActivateChild = function (route, state) {
        return this.canActivate(route, state);
    };
    AuthGuard = __decorate([
        Injectable(), 
        __metadata('design:paramtypes', [Router, AuthService])
    ], AuthGuard);
    return AuthGuard;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/core/auth-guard.service.js.map