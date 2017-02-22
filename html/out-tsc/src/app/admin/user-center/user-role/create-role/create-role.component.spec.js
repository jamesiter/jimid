import { async, TestBed } from '@angular/core/testing';
import { CreateRoleComponent } from './create-role.component';
describe('CreateRoleComponent', function () {
    var component;
    var fixture;
    beforeEach(async(function () {
        TestBed.configureTestingModule({
            declarations: [CreateRoleComponent]
        })
            .compileComponents();
    }));
    beforeEach(function () {
        fixture = TestBed.createComponent(CreateRoleComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', function () {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-role/create-role/create-role.component.spec.js.map