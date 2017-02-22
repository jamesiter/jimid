var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ViewEncapsulation } from '@angular/core';
import { GlobalService } from "../core/global.service";
import { Observable } from "rxjs";
export var UserComponent = (function () {
    function UserComponent(gs) {
        var _this = this;
        this.gs = gs;
        this.Observable = Observable.create(function (observer) {
            _this.gs.roleObserver = observer;
        });
        this.sc = this.Observable.subscribe(function (next) {
            if (next == 1) {
                _this.gs.navigate('/admin');
            }
            _this.sc.unsubscribe();
        }, function (err) {
            console.log(err);
        }, function () {
            _this.sc.unsubscribe();
        });
    }
    UserComponent.prototype.ngOnInit = function () {
        this.gs.getSelfInfo();
    };
    UserComponent = __decorate([
        Component({
            selector: 'app-user',
            templateUrl: './user.component.html',
            styleUrls: [
                '../../assets/src/scss/custom.css',
                './user.component.css',
            ],
            encapsulation: ViewEncapsulation.None
        }), 
        __metadata('design:paramtypes', [GlobalService])
    ], UserComponent);
    return UserComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/user/user.component.js.map