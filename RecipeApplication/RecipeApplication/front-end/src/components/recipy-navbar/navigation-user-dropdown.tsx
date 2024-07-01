import { Button } from "../ui/button";
import Link from "next/link";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger } from "../ui/dropdown-menu";
import { Icons } from "../icons";
import { logout } from "@/lib/utils";
import { navigate } from "@/app/actions";
import { useAuth } from "../providers/auth-provider";
import { Badge } from "../ui/badge";
import UserAvatar from "../user-avatar";

interface NavigationUserDropdownProps {
	
}

export default function NavigationUserDropdown({}: NavigationUserDropdownProps) {

	const { user, setAuth } = useAuth();

	const handleLogout = async () => {
		const logoutResponse = await logout();

		if (!logoutResponse) {
			return;
		}
		setAuth(false);
		navigate("/login");
	}

	const isAdmin = user?.role === "admin";

	const getUserElement = () => {
		if (user) {
			return (
				<DropdownMenu modal={false}>
					<DropdownMenuTrigger>
						<UserAvatar user={user} />
					</DropdownMenuTrigger>
					<DropdownMenuContent side="bottom" align="end" className="*:cursor-pointer">
						<DropdownMenuLabel className="inline-flex items-center space-x-2">
							<UserAvatar user={user} />
							<div className="w">
								<p>{user.firstName} {user.lastName}</p>
								<p className="text-foreground/50 text-xs">{user.email}</p>
							</div>
						</DropdownMenuLabel>
						{ isAdmin && (
							<>
								<DropdownMenuSeparator />
								<DropdownMenuItem className="inline-flex justify-between w-full" asChild>
									<Link href="/admin">
										<p className="inline-flex items-center">
											<Icons.role className="mr-2 w-4 h-4"/>
										Role
										</p>
										<Badge variant="outline">{user.role.toTitleCase()}</Badge>
									</Link>
								</DropdownMenuItem>
							</>
						)}
						<DropdownMenuSeparator />
						<DropdownMenuItem>
							<Icons.user className="mr-2 w-4 h-4"/>
							Profile
						</DropdownMenuItem>
						<DropdownMenuItem>
							<Icons.billing className="mr-2 w-4 h-4"/>
							Billing
						</DropdownMenuItem>
						<DropdownMenuSeparator />
						<DropdownMenuItem onClick={handleLogout} className="text-destructive">
							<Icons.logout className="mr-2 w-4 h-4"/>
							<span>Log out</span>
						</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
			)
		}
		return (
			<Button asChild>
				<Link href="/login">
					Sign in
				</Link>
			</Button>
		)
	}
	
	return getUserElement();
}