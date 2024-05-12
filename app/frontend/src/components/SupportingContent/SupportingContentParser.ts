import DOMPurify from "dompurify";

type ParsedSupportingContentItem = {
    title: string;
    content: string;
};

export function parseSupportingContentItem(parts: any): ParsedSupportingContentItem {
    // Assumes the item starts with the file name followed by : and the content.
    // Example: "sdp_corporate.pdf: this is the content that follows".
    const title = parts["name"];
    const content = DOMPurify.sanitize(parts["description"]);

    return {
        title,
        content,
    };
}
