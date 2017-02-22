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
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/delay';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/switchMap';
import 'rxjs/add/operator/toPromise';
import { Http } from "@angular/http";
import { GlobalService } from "./global.service";
import { Router } from "@angular/router";
export var AuthService = (function () {
    function AuthService(http, gs, router) {
        this.http = http;
        this.gs = gs;
        this.router = router;
        this.Url = '';
        this.isLoggedIn = false;
    }
    AuthService.prototype.login = function (channel, password, login_name, mobile_phone, email) {
        this.payload = { login_name: login_name, password: password, mobile_phone: mobile_phone, email: email };
        if (channel == 'email') {
            this.Url = this.gs.signInByEMailURL;
        }
        else if (channel == 'mobile_phone') {
            this.Url = this.gs.signInByMobilePhoneURL;
        }
        else {
            this.Url = this.gs.signInURL;
        }
        console.log(this.Url);
        return this.http.post(this.Url, this.payload, this.gs.jsonHeadersWithCredentials);
    };
    AuthService.prototype.auth = function () {
        return this.http.get(this.gs.authURL, this.gs.jsonHeadersWithCredentials);
    };
    AuthService.prototype.logout = function () {
        var _this = this;
        this.Url = this.gs.signOutURL;
        var sc = this.http.get(this.Url, this.gs.jsonHeadersWithCredentials).subscribe(function (req) {
            if (req.status == 200) {
                _this.isLoggedIn = false;
                console.log('Logout succeed!');
                _this.router.navigate(['/login']);
            }
            sc.unsubscribe();
        }, function (err) {
            console.log('Logout failed!');
            console.log(err);
        }, function () {
            console.log('Logout complete!');
        });
    };
    AuthService = __decorate([
        Injectable(), 
        __metadata('design:paramtypes', [Http, GlobalService, Router])
    ], AuthService);
    return AuthService;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/core/auth.service.js.map