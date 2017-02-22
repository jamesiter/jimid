var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, EventEmitter, Output } from '@angular/core';
import { Http } from "@angular/http";
import { GlobalService } from "../../../../core/global.service";
import { Role } from "../role";
export var DeleteRoleComponent = (function () {
    function DeleteRoleComponent(http, gs) {
        this.http = http;
        this.gs = gs;
        this.role = new Role();
        this.completed = new EventEmitter();
    }
    DeleteRoleComponent.prototype.ngOnInit = function () {
    };
    DeleteRoleComponent.prototype.show = function (role) {
        this.role = role;
        $('#delete_role_modal').modal('show');
    };
    DeleteRoleComponent.prototype.hide = function () {
        $('#delete_role_modal').modal('hide');
    };
    DeleteRoleComponent.prototype.onSubmit = function () {
        var _this = this;
        var url = this.gs.deleteRoleURL + this.role.id.toString();
        var sc = this.http.delete(url, this.gs.jsonHeadersWithCredentials).subscribe(function (req) {
            sc.unsubscribe();
            _this.completed.emit();
            _this.gs.showingTopFlashMessageSuccess();
        }, function (err) {
            console.log(err);
            _this.gs.showingTopFlashMessageError();
        }, function () {
        });
        this.hide();
    };
    __decorate([
        Output(), 
        __metadata('design:type', Object)
    ], DeleteRoleComponent.prototype, "completed", void 0);
    DeleteRoleComponent = __decorate([
        Component({
            selector: 'app-delete-role',
            templateUrl: './delete-role.component.html',
            styleUrls: ['./delete-role.component.css']
        }), 
        __metadata('design:paramtypes', [Http, GlobalService])
    ], DeleteRoleComponent);
    return DeleteRoleComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-role/delete-role/delete-role.component.js.map