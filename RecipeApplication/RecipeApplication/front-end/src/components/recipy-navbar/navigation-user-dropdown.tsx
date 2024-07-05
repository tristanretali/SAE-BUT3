import { Button } from "../ui/button";
import Link from "next/link";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger } from "../ui/dropdown-menu";
import { Icons } from "../icons";
import { logout } from "@/lib/utils";
import { navigate } from "@/app/actions";
import { useAuth } from "../providers/auth-provider";
import UserAvatar from "../user-avatar";
import { WAGTAIL_URL } from "@/lib/constants";

export default function NavigationUserDropdown() {

	const { user, setAuth } = useAuth();

	const handleLogout = async () => {
		const logoutResponse = await logout();

		if (!logoutResponse) {
			return;
		}
		setAuth(false);
		navigate("/login");
	}

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
								<p>{user.username}</p>
								<p className="text-foreground/50 text-xs">{user.email}</p>
							</div>
						</DropdownMenuLabel>
						<DropdownMenuSeparator />
						{user.superUser && (
							<DropdownMenuItem asChild>
								<Link href={`${WAGTAIL_URL}/admin`}>
									<Icons.role className="mr-2 w-4 h-4"/>
									Admin panel
								</Link>
							</DropdownMenuItem>
						)}
						<DropdownMenuItem disabled={true}>
							<Icons.user className="mr-2 w-4 h-4"/>
							Profile
						</DropdownMenuItem>
						<DropdownMenuItem asChild>
							<Link href="/favorites">
								<Icons.like className="mr-2 w-4 h-4"/>
								Favourites
							</Link>
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