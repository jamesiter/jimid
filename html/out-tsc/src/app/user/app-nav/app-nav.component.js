var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component } from '@angular/core';
import { Http } from "@angular/http";
import { GlobalService } from "../../core/global.service";
export var AppNavComponent = (function () {
    function AppNavComponent(http, gs) {
        this.http = http;
        this.gs = gs;
        this.appList = [];
    }
    AppNavComponent.prototype.ngOnInit = function () {
    };
    AppNavComponent.prototype.ngAfterViewInit = function () {
        this.getAppList();
    };
    AppNavComponent.prototype.getAppList = function () {
        var _this = this;
        var sc = this.http.get(this.gs.getSelfAppListURL + '?order_by=create_time', { withCredentials: true }).subscribe(function (req) {
            if (req.status == 200) {
                var data = req.json();
                _this.appList = data.data;
                sc.unsubscribe();
            }
        }, function (err) {
            console.log(err);
        }, function () {
        });
    };
    AppNavComponent = __decorate([
        Component({
            selector: 'app-app-nav',
            templateUrl: './app-nav.component.html',
            styleUrls: ['./app-nav.component.css']
        }), 
        __metadata('design:paramtypes', [Http, GlobalService])
    ], AppNavComponent);
    return AppNavComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/user/app-nav/app-nav.component.js.map