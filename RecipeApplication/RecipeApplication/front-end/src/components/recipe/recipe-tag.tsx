import { cn } from "@/lib/utils";

type RecipeTagProps = {
	children: React.ReactNode;
	className?: string;
};

export function RecipeTag({children, className}: RecipeTagProps) {
	return (
		<div className={cn("rounded-md inline-flex justify-center items-center space-x-1 bg-slate-200 text-sm font-medium p-2 w-20", className)}>
			{children}
		</div>
	)
}