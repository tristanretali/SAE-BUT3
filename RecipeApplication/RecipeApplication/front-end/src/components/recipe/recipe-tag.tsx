import { cn } from "@/lib/utils";

type RecipeTagProps = {
	children: React.ReactNode;
	value?: string | number;
	valueSuffix?: string;
	className?: string;
};

export function RecipeTag({children, className, value, valueSuffix}: RecipeTagProps) {

	if (!value) return null;

	return (
		<div className={cn("rounded-md inline-flex justify-center items-center space-x-1 bg-slate-200 text-sm font-medium p-2 w-24", className)}>
			{children}
			<p className="truncate">{value}{valueSuffix}</p>
		</div>
	)
}