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
import { AdminComponent } from './admin.component';
import { AdminRoutingModule } from "./admin-routing.module";
import { FooterComponent } from "./footer/footer.component";
import { SidebarMenuComponent } from "./sidebar-menu/sidebar-menu.component";
import { FooterMenuComponent } from "./footer-menu/footer-menu.component";
import { TopNavComponent } from "./top-nav/top-nav.component";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { UserCenterModule } from "./user-center/user-center.module";
import { AppManageModule } from "./app-manage/app-manage.module";
export var AdminModule = (function () {
    function AdminModule() {
    }
    AdminModule = __decorate([
        NgModule({
            imports: [
                CommonModule,
                UserCenterModule,
                AppManageModule,
                AdminRoutingModule
            ],
            declarations: [
                FooterComponent,
                SidebarMenuComponent,
                FooterMenuComponent,
                TopNavComponent,
                DashboardComponent,
                AdminComponent
            ]
        }), 
        __metadata('design:paramtypes', [])
    ], AdminModule);
    return AdminModule;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/admin.module.js.map