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
import { User } from "../user";
import { Http } from "@angular/http";
import { GlobalService } from "../../../../core/global.service";
export var DeleteUserComponent = (function () {
    function DeleteUserComponent(http, gs) {
        this.http = http;
        this.gs = gs;
        this.user = new User();
        this.completed = new EventEmitter();
    }
    DeleteUserComponent.prototype.ngOnInit = function () {
    };
    DeleteUserComponent.prototype.show = function (user) {
        this.user = user;
        $('#delete_user_modal').modal('show');
    };
    DeleteUserComponent.prototype.hide = function () {
        $('#delete_user_modal').modal('hide');
    };
    DeleteUserComponent.prototype.onSubmit = function () {
        var _this = this;
        var url = this.gs.deleteUserURL + this.user.id.toString();
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
    ], DeleteUserComponent.prototype, "completed", void 0);
    DeleteUserComponent = __decorate([
        Component({
            selector: 'app-delete-user',
            templateUrl: './delete-user.component.html',
            styleUrls: ['./delete-user.component.css']
        }), 
        __metadata('design:paramtypes', [Http, GlobalService])
    ], DeleteUserComponent);
    return DeleteUserComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-list/delete-user/delete-user.component.js.map