""
import { RecipesCount } from "@/components/recipe/recipe-count";
import { Searchbar } from "@/components/searchbar";
import { Badge } from "@/components/ui/badge";
import Image from "next/image";

export default function Home() {

	return (
		<div className="inline-flex justify-center items-center space-x-10 w-3/4 h-3/4 justify-self-center">
			<div className="flex flex-col items-center space-y-5 md:items-start text-center md:text-start">
				<Badge variant="secondary" className="px-2 py-[5px] text-lime-900">🌍 Recipes from all around the globe!</Badge>
				<h1 className="font-heading text-5xl text-slate-700">
					Bring your tastes to the next level with Recipy
				</h1>
				<div className="text-gray-500 text-sm md:text-lg md:w-auto inline-block">
					Our application has more than
					<RecipesCount/>
					recipes that you can use to cook better!
				</div>
				<Searchbar className="w-80 md:w-96"/>
			</div>
			<Image src="/illustration-landingpage.png" alt="Illustration" width={500} height={500} className="hidden md:flex"/>
		</div>
	);
}
