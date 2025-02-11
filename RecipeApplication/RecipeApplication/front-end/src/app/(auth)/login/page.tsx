import { Icons } from "@/components/icons";
import { buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { LoginForm } from "@/components/forms/login-form";

import Link from "next/link";
import { Logo } from "@/components/logo";

export default function LoginPage() {

	return (
		<div className="container flex h-screen w-screen flex-col items-center justify-center">
			<Link
				href="/"
				className={cn(
					buttonVariants({ variant: "ghost" }),
					"absolute left-4 top-4 md:left-8 md:top-8"
				)}
			>
				<Icons.chevronLeft className="mr-2 h-4 w-4" />
				Back
			</Link>
			<div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
				<Logo size={50} className="mx-auto"/>
				<div className="flex flex-col space-y-2 text-center">
					<h1 className="text-2xl font-semibold tracking-tight">
						Welcome back
					</h1>
					<p className="text-sm text-muted-foreground">
						Enter your credentials to continue
					</p>
				</div>
				<LoginForm/>
				<p className="px-8 text-center text-sm text-muted-foreground">
					<Link
						href="/register"
						className="hover:text-brand underline underline-offset-4"
					>
						Don&apos;t have an account? Register
					</Link>
				</p>
			</div>
		</div>
	);
}