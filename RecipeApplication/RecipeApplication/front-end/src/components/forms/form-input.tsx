import { FormControl, FormItem, FormLabel, FormMessage, useFormField } from "@/components/ui/form"

type FormFieldProps = {
    children: React.ReactNode
    label?: string
}

export function FormInput({children, label} : FormFieldProps) {

	const { name } = useFormField()

	return (
		<FormItem>
			<FormLabel>{label || name.toTitleCase()}</FormLabel>
			<FormControl>
				{children}
			</FormControl>
			<FormMessage/>
		</FormItem>
	)
}