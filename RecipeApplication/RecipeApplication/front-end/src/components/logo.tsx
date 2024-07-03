import { cn } from "@/lib/utils";
import Image from "next/image";
import Link from "next/link";

interface LogoProps {
	className?: string;
	size: number;
	withText?: boolean;
}

export function Logo({ className, withText = false, size }: LogoProps) {
  
	return (
		<Link className={cn("inline-flex items-center space-x-2", className)} href="/">
			<Image src="/logo-recipy.png" alt="Anemone" width={size} height={size}/>
			{withText && <span className="text-md font-extrabold text-[#2E2E2E]">Recipy</span>}
		</Link>
	)
}