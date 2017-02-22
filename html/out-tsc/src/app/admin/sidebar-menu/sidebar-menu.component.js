var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component } from '@angular/core';
export var SidebarMenuComponent = (function () {
    function SidebarMenuComponent() {
    }
    SidebarMenuComponent.prototype.ngOnInit = function () {
    };
    SidebarMenuComponent.prototype.ngAfterViewInit = function () {
        this.sidebarMenu = $('#sidebar-menu');
    };
    SidebarMenuComponent.prototype.anchorClicked = function (event) {
        this.li = $(event.toElement).parent();
        if (!this.li.is('.active')) {
            if (!this.li.parent().is('.child_menu')) {
                this.sidebarMenu.find('li').removeClass('active active-sm');
                this.sidebarMenu.find('li ul').slideUp();
            }
            this.li.addClass('active');
            $('ul:first', this.li).slideDown();
        }
        else {
            this.li.removeClass('active active-sm');
            $('ul:first', this.li).slideUp();
        }
    };
    SidebarMenuComponent = __decorate([
        Component({
            selector: 'app-sidebar-menu',
            templateUrl: './sidebar-menu.component.html',
            styleUrls: ['./sidebar-menu.component.css']
        }), 
        __metadata('design:paramtypes', [])
    ], SidebarMenuComponent);
    return SidebarMenuComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/sidebar-menu/sidebar-menu.component.js.map