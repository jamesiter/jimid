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
import { UserCenterComponent } from './user-center.component';
import { UserListComponent } from "./user-list/user-list.component";
import { UserLogComponent } from "./user-log/user-log.component";
import { FormsModule } from "@angular/forms";
import { CreateUserComponent } from "./user-list/create-user/create-user.component";
import { EditUserComponent } from "./user-list/edit-user/edit-user.component";
import { DeleteUserComponent } from "./user-list/delete-user/delete-user.component";
import { ResetPasswordComponent } from "./user-list/reset-password/reset-password.component";
import { UserRoleComponent } from "./user-role/user-role.component";
import { CreateRoleComponent } from "./user-role/create-role/create-role.component";
import { EditRoleComponent } from "./user-role/edit-role/edit-role.component";
import { EditRoleMemberComponent } from "./user-role/edit-role-member/edit-role-member.component";
import { EditRoleAppComponent } from "./user-role/edit-role-app/edit-role-app.component";
import { DeleteRoleComponent } from "./user-role/delete-role/delete-role.component";
export var UserCenterModule = (function () {
    function UserCenterModule() {
    }
    UserCenterModule = __decorate([
        NgModule({
            imports: [
                CommonModule,
                FormsModule
            ],
            declarations: [
                UserCenterComponent,
                UserListComponent, CreateUserComponent, EditUserComponent, DeleteUserComponent, ResetPasswordComponent,
                UserLogComponent,
                UserRoleComponent, CreateRoleComponent, EditRoleComponent, EditRoleMemberComponent, EditRoleAppComponent,
                DeleteRoleComponent
            ]
        }), 
        __metadata('design:paramtypes', [])
    ], UserCenterModule);
    return UserCenterModule;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-center.module.js.map