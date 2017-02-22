import { async, TestBed } from '@angular/core/testing';
import { SidebarMenuComponent } from './sidebar-menu.component';
describe('SidebarMenuComponent', function () {
    var component;
    var fixture;
    beforeEach(async(function () {
        TestBed.configureTestingModule({
            declarations: [SidebarMenuComponent]
        })
            .compileComponents();
    }));
    beforeEach(function () {
        fixture = TestBed.createComponent(SidebarMenuComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', function () {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/sidebar-menu/sidebar-menu.component.spec.js.map