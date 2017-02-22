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
import { GlobalService } from "../../../core/global.service";
export var UserRoleComponent = (function () {
    function UserRoleComponent(http, gs) {
        this.http = http;
        this.gs = gs;
        this.roles = [];
    }
    UserRoleComponent.prototype.ngOnInit = function () {
    };
    UserRoleComponent.prototype.ngAfterViewInit = function () {
        this.getRoles();
    };
    UserRoleComponent.prototype.getRoles = function () {
        var _this = this;
        var sc = this.http.get(this.gs.getUserRoleAppMappingURL, { withCredentials: true }).subscribe(function (req) {
            if (req.status == 200) {
                var data = req.json();
                _this.roles = data.data;
                sc.unsubscribe();
            }
        }, function (err) {
            console.log(err);
        }, function () {
        });
    };
    UserRoleComponent = __decorate([
        Component({
            selector: 'app-user-role',
            templateUrl: './user-role.component.html',
            styleUrls: ['./user-role.component.css']
        }), 
        __metadata('design:paramtypes', [Http, GlobalService])
    ], UserRoleComponent);
    return UserRoleComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-role/user-role.component.js.map