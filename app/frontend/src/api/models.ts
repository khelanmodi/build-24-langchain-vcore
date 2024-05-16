export const enum RetrievalMode {
    Hybrid = "rag",
    Vectors = "vector",
    Text = "keyword"
}

export type ChatAppRequestOverrides = {
    retrieval_mode?: RetrievalMode;
    top?: number;
    temperature?: number;
    score_threshold?: number;
};

export type ResponseMessage = {
    content: string;
    role: string;
};

export type Thoughts = {
    title: string;
    description: any; // It can be any output from the api
    props?: { [key: string]: string };
};

export type ResponseContext = {
    data_points: any[];
    thoughts: Thoughts[];
};

export type ResponseChoice = {
    index: number;
    message: ResponseMessage;
    context: ResponseContext;
};

export type ChatAppResponseOrError = {
    choices?: ResponseChoice[];
    error?: string;
};

export type ChatAppResponse = {
    choices: ResponseChoice[];
};

export type ChatAppRequestContext = {
    overrides?: ChatAppRequestOverrides;
};

export type ChatAppRequest = {
    messages: ResponseMessage[];
    context?: ChatAppRequestContext;
    stream?: boolean;
};

export type SimpleAPIResponse = {
    message?: string;
};
