import { UserLogComponent } from "./user-log/user-log.component";
import { UserListComponent } from "./user-list/user-list.component";
import { UserRoleComponent } from "./user-role/user-role.component";
/**
 * Created by James on 2016/12/14.
 */
export var userCenterRoutes = [
    { path: 'user-list', component: UserListComponent },
    { path: 'user-log', component: UserLogComponent },
    { path: 'user-role', component: UserRoleComponent },
    { path: '', redirectTo: 'user-list', pathMatch: 'full' },
];
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-center-routing.module.js.map