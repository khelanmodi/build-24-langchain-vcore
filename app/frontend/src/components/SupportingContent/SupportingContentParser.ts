import DOMPurify from "dompurify";

type ParsedSupportingContentItem = {
    title: string;
    content: string;
    category: string;
    collection: string;
    price: string;
};

export function parseSupportingContentItem(parts: any): ParsedSupportingContentItem {
    // Assumes the item starts with the file name followed by : and the content.
    // Example: "sdp_corporate.pdf: this is the content that follows".
    const title = parts["name"];
    const category = parts["category"];
    const collection = parts["collection"];
    const price = parts["price"];
    const content = DOMPurify.sanitize(parts["description"]);

    return {
        title,
        content,
        category,
        collection,
        price,
    };
}
