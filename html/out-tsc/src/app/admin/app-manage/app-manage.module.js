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
import { FormsModule } from "@angular/forms";
import { AppManageComponent } from "./app-manage.component";
import { AppListComponent } from "./app-list/app-list.component";
import { CreateAppComponent } from "./app-list/create-app/create-app.component";
import { DeleteAppComponent } from "./app-list/delete-app/delete-app.component";
import { OpenidComponent } from "./openid/openid.component";
import { EditOpenidComponent } from "./openid/edit-openid/edit-openid.component";
import { DeleteOpenidComponent } from "./openid/delete-openid/delete-openid.component";
import { EditAppComponent } from "./app-list/edit-app/edit-app.component";
export var AppManageModule = (function () {
    function AppManageModule() {
    }
    AppManageModule = __decorate([
        NgModule({
            imports: [
                CommonModule,
                FormsModule
            ],
            declarations: [
                AppManageComponent,
                AppListComponent, CreateAppComponent, DeleteAppComponent, EditAppComponent,
                OpenidComponent, EditOpenidComponent, DeleteOpenidComponent
            ]
        }), 
        __metadata('design:paramtypes', [])
    ], AppManageModule);
    return AppManageModule;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/app-manage/app-manage.module.js.map