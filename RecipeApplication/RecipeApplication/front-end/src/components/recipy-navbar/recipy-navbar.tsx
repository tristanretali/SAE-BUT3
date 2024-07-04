"use client"

import { WAGTAIL_URL } from "@/lib/constants";
import { Logo } from "../logo";
import { NavigationMenu, NavigationMenuItem, NavigationMenuList } from "../ui/navigation-menu";
import { Separator } from "../ui/separator";
import { NavigationLink } from "./navigation-link";
import NavigationUserDropdown from "./navigation-user-dropdown";

export function RecipyNavbar() {

	return (
		<>
			<NavigationMenu className="h-20 justify-between max-w-full px-4 py-5">
				<NavigationMenuList>
					<NavigationMenuItem className="inline-flex">
						<Logo withText={true} size={35}/>
					</NavigationMenuItem>
				</NavigationMenuList>
				<NavigationMenuList	 className="space-x-6">
				</NavigationMenuList>
				<NavigationMenuList className="space-x-7">
					<NavigationLink href={`${WAGTAIL_URL}/admin/snippets/recipe/recipe/add/`} className="text-primary/80">
						Suggest a recipe
					</NavigationLink>
					<NavigationMenuItem className="inline-flex">
						<NavigationUserDropdown />
					</NavigationMenuItem>
				</NavigationMenuList>
			</NavigationMenu>
			<Separator/>
		</>
	)
}