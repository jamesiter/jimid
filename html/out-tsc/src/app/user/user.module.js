var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserComponent } from './user.component';
import { UserRoutingModule } from "./user-routing.module";
import { UserTopNavComponent } from "./user-top-nav/user-top-nav.component";
import { UserFooterComponent } from "./user-footer/user-footer.component";
import { AppNavComponent } from "./app-nav/app-nav.component";
export var UserModule = (function () {
    function UserModule() {
    }
    UserModule = __decorate([
        NgModule({
            imports: [
                CommonModule,
                UserRoutingModule
            ],
            declarations: [
                UserComponent,
                UserTopNavComponent,
                UserFooterComponent,
                AppNavComponent
            ]
        }), 
        __metadata('design:paramtypes', [])
    ], UserModule);
    return UserModule;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/user/user.module.js.map