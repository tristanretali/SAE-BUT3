import { NavigationMenuItem, NavigationMenuLink } from "@/components/ui/navigation-menu";
import { cn } from "@/lib/utils";
import Link from "next/link";
import { Icons } from "../icons";

interface NavigationLinkProps {
	href: string;
	className?: string;
	icon?: keyof typeof Icons;
	children: React.ReactNode;
}

export function NavigationLink({ href, children, className, icon }: NavigationLinkProps) {

	const Icon = icon ? Icons[icon]: null;

	return (
		<NavigationMenuItem className="inline-flex">
			<Link href={href} legacyBehavior passHref>
				<NavigationMenuLink 
					className={cn(
						"text-lg font-medium gap-2 transition-colors sm:text-sm w-full py-3 px-2",
						className,
					)}>
					{Icon && <Icon className={cn("h-5")}/>}
					{children}
				</NavigationMenuLink>
			</Link>
		</NavigationMenuItem>
	);
}