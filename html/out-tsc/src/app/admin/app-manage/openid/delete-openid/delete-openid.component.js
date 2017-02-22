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
import { Openid } from "../openid";
import { App } from "../../app-list/app";
import { User } from "../../../user-center/user-list/user";
export var DeleteOpenidComponent = (function () {
    function DeleteOpenidComponent(http, gs) {
        this.http = http;
        this.gs = gs;
        this.openid = new Openid();
        this.completed = new EventEmitter();
        this.openid.app = new App();
        this.openid.user = new User();
    }
    DeleteOpenidComponent.prototype.ngOnInit = function () {
    };
    DeleteOpenidComponent.prototype.show = function (openid) {
        this.openid = openid;
        $('#delete_openid_modal').modal('show');
    };
    DeleteOpenidComponent.prototype.hide = function () {
        $('#delete_openid_modal').modal('hide');
    };
    DeleteOpenidComponent.prototype.onSubmit = function () {
        var _this = this;
        var url = this.gs.deleteOpenidURL + this.openid.appid.toString() + '/' + this.openid.uid.toString();
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
    ], DeleteOpenidComponent.prototype, "completed", void 0);
    DeleteOpenidComponent = __decorate([
        Component({
            selector: 'app-delete-openid',
            templateUrl: './delete-openid.component.html',
            styleUrls: ['./delete-openid.component.css']
        }), 
        __metadata('design:paramtypes', [Http, GlobalService])
    ], DeleteOpenidComponent);
    return DeleteOpenidComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/app-manage/openid/delete-openid/delete-openid.component.js.map