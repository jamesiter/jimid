import { async, TestBed } from '@angular/core/testing';
import { DeleteRoleComponent } from './delete-role.component';
describe('DeleteRoleComponent', function () {
    var component;
    var fixture;
    beforeEach(async(function () {
        TestBed.configureTestingModule({
            declarations: [DeleteRoleComponent]
        })
            .compileComponents();
    }));
    beforeEach(function () {
        fixture = TestBed.createComponent(DeleteRoleComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', function () {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-role/delete-role/delete-role.component.spec.js.map