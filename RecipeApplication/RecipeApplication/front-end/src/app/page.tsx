import { RecipyNavbar } from "@/components/recipy-navbar/recipy-navbar";
import { Searchbar } from "@/components/searchbar";
import { Badge } from "@/components/ui/badge";
import Image from "next/image";

export default function Home() {
  return (
	<div className="container border-x-[1px] border-dashed px-0 h-screen flex flex-col">
		<RecipyNavbar />
		<main className="flex flex-col items-center h-3/4 justify-center">
			<div className="inline-flex justify-center items-center space-x-10 w-3/4">
				<div className="flex flex-col items-start space-y-5">
					<Badge variant="secondary" className="px-2 py-[5px] text-lime-900">🌍 Recipes from all around the globe!</Badge>
					<h1 className="font-heading text-5xl text-slate-700">
						Bring your tastes to the next level with Recipy
					</h1>
					<p className="text-gray-500">Our application has more than <span className="text-primary font-bold">10.000</span> recipes that you can use to cook better!</p>
					<Searchbar className="w-96"/>
				</div>
				<Image src="/illustration-landingpage.png" alt="Illustration" width={500} height={500}/>
			</div>
		</main>
    </div>
  );
}
