var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { AppComponent } from './app.component';
import { AppRoutingModule } from "./app-routing.module";
import { AuthService } from "./core/auth.service";
import { AuthGuard } from "./core/auth-guard.service";
import { LoginComponent } from './login/login.component';
import { AdminModule } from "./admin/admin.module";
import { GlobalService } from "./core/global.service";
import { UserModule } from "./user/user.module";
export var AppModule = (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        NgModule({
            declarations: [
                AppComponent,
                LoginComponent
            ],
            imports: [
                BrowserModule,
                FormsModule,
                HttpModule,
                AdminModule,
                UserModule,
                AppRoutingModule,
            ],
            providers: [
                { provide: Window, useValue: window },
                GlobalService,
                AuthService,
                AuthGuard,
            ],
            bootstrap: [AppComponent]
        }), 
        __metadata('design:paramtypes', [])
    ], AppModule);
    return AppModule;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/app.module.js.map