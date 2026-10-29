import { test, expect, Locator } from '@playwright/test';
import { text } from 'node:stream/consumers';

// ctrl+shift+p : emulate focus page
//Auto Suggest Dropdown | Hidden Dropdown | Dynamic Dropdown | Without select tag Dropdown
test("Auto Suggest | Dynamic | Hidden Dropdown",async({page})=>{
    await page.goto("https://www.flipkart.com/");

    await page.waitForTimeout(3000);

    await page.locator('.b3wTlE').click({ timeout: 3000 }).catch(() => {});

    await page.waitForTimeout(2000);
    
    //Search text : not exist readonly attribute
    await page.locator("input[name='q']:not([readonly])").fill("smart")

    
    await page.waitForTimeout(2000);
    //Get all suggest options : Ctrl+Shift+P : Emulate Focused Page
    const options:Locator = await page.locator("ul>li")
    await page.waitForTimeout(2000);
    const count = await options.count();

    console.log("number of suggested options===",count);
    
    // find out nth() options
    console.log("Nth 5 Number option",await options.nth(5).innerText())

    //print all auto suggest value
    for(let i=0;i<count;i++){
        console.log(await options.nth(i).textContent())
    }

    //select/click on smartphone option
    for(let i=0;i<count;i++){
        const nText = await options.nth(i).innerText();
        if(nText=='smartphone'){
            options.nth(i).click();
            break;
        }
    }

})