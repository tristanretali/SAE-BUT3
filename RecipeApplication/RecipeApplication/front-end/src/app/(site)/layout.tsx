import { RecipyNavbar } from "@/components/recipy-navbar/recipy-navbar";

export default function SiteLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

	return (
		<div className="container border-x-[1px] border-dashed px-0 h-screen flex flex-col">
			<RecipyNavbar />
			<main className="h-full w-full flex justify-center">
				{children}
			</main>
		</div>
	)
}