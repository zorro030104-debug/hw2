#!/usr/bin/env python3
"""Simple CLI prototype: complaint -> internal escalation summary."""

import argparse
import os
import sys

from openai import OpenAI

DEFAULT_SYSTEM_PROMPT = (
    "You are an internal escalation writer for an e-commerce support team. "
    "Read the customer complaint and return a concise escalation summary with "
    "the following sections: Problem, Impact, Recommended action. "
    "Use only information from the complaint. If details are unclear or "
    "contradictory, request human review instead of making up facts."
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Turn a customer complaint into an internal escalation summary."
    )
    parser.add_argument(
        "complaint",
        nargs="*",
        help="Customer complaint text. If omitted, the script prompts for it.",
    )
    parser.add_argument(
        "--system-prompt",
        default=None,
        help="Optional custom system prompt for the LLM.",
    )
    return parser.parse_args()


def build_message(complaint: str, system_prompt: str) -> str:
    return complaint.strip()


def call_llm(system_prompt: str, complaint: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it before running this script."
        )

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": build_message(complaint, system_prompt)},
        ],
        max_tokens=300,
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()


def main():
    args = parse_args()
    complaint = " ".join(args.complaint).strip() if args.complaint else ""

    if not complaint:
        complaint = input("Enter customer complaint: ").strip()

    if not complaint:
        print("No customer complaint was provided. Exiting.")
        return

    system_prompt = args.system_prompt or DEFAULT_SYSTEM_PROMPT

    print("\n=== Complaint ===")
    print(complaint)
    print("\n=== System Prompt ===")
    print(system_prompt)

    try:
        summary = call_llm(system_prompt, complaint)
        print("\n=== Escalation Summary ===")
        print(summary)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
