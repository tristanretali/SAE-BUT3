import { Icons } from "@/components/icons";
import { buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";

import Link from "next/link";
import { Logo } from "@/components/logo";
import { RegisterForm } from "@/components/forms/register-form";

export default function RegisterPage() {

	return (
		<div className="flex h-screen w-screen flex-row items-center justify-center">
			<div className="w-1/2 h-full bg-primary">

			</div>
			<div className="flex-1">
				<Link
					href="/"
					className={cn(
						buttonVariants({ variant: "ghost" }),
						"text-white",
						"absolute left-4 top-4 md:left-8 md:top-8"
					)}
				>
					<Icons.chevronLeft className="mr-2 h-4 w-4" />
				Back
				</Link>
				<div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[400px]">
					<Logo size={50} className="mx-auto"/>
					<div className="flex flex-col space-y-2 text-center">
						<h1 className="text-2xl font-semibold tracking-tight">
						Welcome !
						</h1>
						<p className="text-sm text-muted-foreground">
						Please register to continue
						</p>
					</div>
					<RegisterForm/>
				</div>
			</div>
		</div>
	);
}