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
export var TopNavComponent = (function () {
    /*
    private topNavTipObservable: Observable<string>;
    private sc;
    */
    function TopNavComponent(authService, gs) {
        this.authService = authService;
        this.gs = gs;
        this.login_name = '';
        /* this.topNavTipObservable = Observable.create((observer:Observer<string>) => {
          this.gs.topNavTipObserver = observer;
        });
        this.sc = this.topNavTipObservable.subscribe(
          (next) => {
    
          },
          (err) => {
            console.log(err);
          },
          () => {
            this.sc.unsubscribe();
          }
        )*/
    }
    TopNavComponent.prototype.ngOnInit = function () {
    };
    TopNavComponent.prototype.logout = function () {
        this.authService.logout();
    };
    __decorate([
        Input(), 
        __metadata('design:type', String)
    ], TopNavComponent.prototype, "login_name", void 0);
    TopNavComponent = __decorate([
        Component({
            selector: 'app-top-nav',
            templateUrl: './top-nav.component.html',
            styleUrls: ['./top-nav.component.css'],
        }), 
        __metadata('design:paramtypes', [AuthService, GlobalService])
    ], TopNavComponent);
    return TopNavComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/top-nav/top-nav.component.js.map