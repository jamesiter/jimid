var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input } from '@angular/core';
import { AuthService } from "../../core/auth.service";
import { GlobalService } from "../../core/global.service";
export var UserTopNavComponent = (function () {
    function UserTopNavComponent(authService, gs) {
        this.authService = authService;
        this.gs = gs;
        this.login_name = '';
    }
    UserTopNavComponent.prototype.ngOnInit = function () {
    };
    UserTopNavComponent.prototype.logout = function () {
        this.authService.logout();
    };
    __decorate([
        Input(), 
        __metadata('design:type', String)
    ], UserTopNavComponent.prototype, "login_name", void 0);
    UserTopNavComponent = __decorate([
        Component({
            selector: 'app-user-top-nav',
            templateUrl: './user-top-nav.component.html',
            styleUrls: ['./user-top-nav.component.css']
        }), 
        __metadata('design:paramtypes', [AuthService, GlobalService])
    ], UserTopNavComponent);
    return UserTopNavComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/user/user-top-nav/user-top-nav.component.js.map